import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import logging
from typing import Dict, List, Tuple
import csv
from datetime import datetime
from config import PAIN_CLUSTERS, LIFECYCLE_STAGES, ICPS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentAnalyzer:
    def __init__(self):
        self.pain_clusters = PAIN_CLUSTERS
        self.lifecycle_stages = LIFECYCLE_STAGES
        self.icps = ICPS
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def scrape_content(self, url: str) -> Dict[str, str]:
        """Scrape content from a given URL."""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            for script in soup(['script', 'style']):
                script.decompose()
            
            title = soup.find('h1')
            title = title.get_text(strip=True) if title else (soup.title.string if soup.title else "No title")
            
            text = soup.get_text(separator=' ', strip=True)
            
            return {
                'url': url,
                'title': title,
                'text': text,
                'domain': urlparse(url).netloc,
                'scraped_at': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            return None

    def identify_pain_cluster(self, text: str) -> Tuple[str, float]:
        """Identify the primary pain cluster and confidence score."""
        cluster_scores = {}
        text_lower = text.lower()
        
        for cluster, config in self.pain_clusters.items():
            score = 0
            
            for keyword in config['keywords']:
                if keyword.lower() in text_lower:
                    score += text_lower.count(keyword.lower())
            
            for subcategory in config['subcategories']:
                if subcategory.lower() in text_lower:
                    score += 5
            
            cluster_scores[cluster] = score
        
        if not cluster_scores or sum(cluster_scores.values()) == 0:
            return "Unclassified", 0.0
        
        primary_cluster = max(cluster_scores, key=cluster_scores.get)
        total_score = sum(cluster_scores.values())
        confidence = cluster_scores[primary_cluster] / total_score if total_score > 0 else 0
        
        return primary_cluster, min(confidence, 1.0)

    def identify_lifecycle_stage(self, text: str) -> Tuple[str, float]:
        """Identify the primary lifecycle stage and confidence score."""
        stage_scores = {}
        text_lower = text.lower()
        
        for stage, config in self.lifecycle_stages.items():
            score = 0
            for keyword in config['keywords']:
                if keyword.lower() in text_lower:
                    score += text_lower.count(keyword.lower())
            stage_scores[stage] = score
        
        if not stage_scores or sum(stage_scores.values()) == 0:
            return "Unknown", 0.0
        
        primary_stage = max(stage_scores, key=stage_scores.get)
        total_score = sum(stage_scores.values())
        confidence = stage_scores[primary_stage] / total_score if total_score > 0 else 0
        
        return primary_stage, min(confidence, 1.0)

    def identify_icp(self, text: str) -> Tuple[str, float]:
        """Identify the primary ICP and confidence score."""
        icp_scores = {}
        text_lower = text.lower()
        
        for icp, config in self.icps.items():
            score = 0
            for keyword in config['keywords']:
                if keyword.lower() in text_lower:
                    score += text_lower.count(keyword.lower())
            
            for characteristic in config['characteristics']:
                if characteristic.lower() in text_lower:
                    score += 3
            
            icp_scores[icp] = score
        
        if not icp_scores or sum(icp_scores.values()) == 0:
            return "Unidentified", 0.0
        
        primary_icp = max(icp_scores, key=icp_scores.get)
        total_score = sum(icp_scores.values())
        confidence = icp_scores[primary_icp] / total_score if total_score > 0 else 0
        
        return primary_icp, min(confidence, 1.0)

    def analyze_url(self, url: str) -> Dict:
        """Complete analysis pipeline for a URL."""
        content = self.scrape_content(url)
        if not content:
            return {
                'url': url,
                'status': 'error',
                'error': 'Failed to scrape content'
            }
        
        pain_cluster, cluster_confidence = self.identify_pain_cluster(content['text'])
        lifecycle_stage, stage_confidence = self.identify_lifecycle_stage(content['text'])
        icp, icp_confidence = self.identify_icp(content['text'])
        
        return {
            'url': url,
            'title': content['title'],
            'domain': content['domain'],
            'status': 'success',
            'pain_cluster': pain_cluster,
            'pain_cluster_confidence': round(cluster_confidence, 3),
            'lifecycle_stage': lifecycle_stage,
            'lifecycle_stage_confidence': round(stage_confidence, 3),
            'icp': icp,
            'icp_confidence': round(icp_confidence, 3),
            'analyzed_at': datetime.now().isoformat()
        }

    def analyze_urls(self, urls: List[str]) -> List[Dict]:
        """Analyze multiple URLs and return results."""
        results = []
        for i, url in enumerate(urls, 1):
            logger.info(f"Analyzing URL {i}/{len(urls)}: {url}")
            result = self.analyze_url(url)
            results.append(result)
        return results

    def save_to_csv(self, results: List[Dict], output_file: str = 'content_analysis.csv'):
        """Save analysis results to CSV file."""
        if not results:
            logger.warning("No results to save")
            return
        
        valid_results = [r for r in results if r.get('status') == 'success']
        
        if not valid_results:
            logger.warning("No valid results to save")
            return
        
        fieldnames = [
            'url',
            'title',
            'domain',
            'pain_cluster',
            'pain_cluster_confidence',
            'lifecycle_stage',
            'lifecycle_stage_confidence',
            'icp',
            'icp_confidence',
            'analyzed_at'
        ]
        
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for result in valid_results:
                    writer.writerow({k: result.get(k, '') for k in fieldnames})
            
            logger.info(f"Results saved to {output_file}")
        except Exception as e:
            logger.error(f"Error saving to CSV: {str(e)}")
