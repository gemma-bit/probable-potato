#!/usr/bin/env python3
"""
Content Analyzer - Main Entry Point
Scrapes URLs and classifies content by pain clusters, lifecycle stages, and ICP.
"""

from content_analyzer import ContentAnalyzer
import sys

def main():
    analyzer = ContentAnalyzer()
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <url1> <url2> <url3> ...")
        print("\nExample:")
        print("python main.py https://example.com/article1 https://example.com/article2")
        return
    
    urls = sys.argv[1:]
    
    print(f"\nAnalyzing {len(urls)} URL(s)...\n")
    results = analyzer.analyze_urls(urls)
    
    print("\n" + "="*100)
    print("ANALYSIS RESULTS")
    print("="*100 + "\n")
    
    for result in results:
        print(f"URL: {result['url']}")
        print(f"Title: {result['title']}")
        
        if result.get('status') == 'error':
            print(f"Status: ERROR - {result.get('error')}")
        else:
            print(f"Domain: {result['domain']}")
            print(f"Pain Cluster: {result['pain_cluster']} (confidence: {result['pain_cluster_confidence']})")
            print(f"Lifecycle Stage: {result['lifecycle_stage']} (confidence: {result['lifecycle_stage_confidence']})")
            print(f"ICP: {result['icp']} (confidence: {result['icp_confidence']})")
        
        print("-" * 100 + "\n")
    
    analyzer.save_to_csv(results)
    print("✅ Results saved to content_analysis.csv")

if __name__ == "__main__":
    main()
