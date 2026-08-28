# Pain Clusters Definition
PAIN_CLUSTERS = {
    "Draw and Loan Operations": {
        "subcategories": [
            "Draw management",
            "Draw inspections",
            "Activity tracking",
            "Operational execution"
        ],
        "keywords": [
            "draw", "disbursement", "draw request", "draw management", "draw inspections",
            "inspection", "activity tracking", "execution", "loan operations", 
            "fund release", "fund distribution", "operational workflow", "draw schedule",
            "milestones", "draw cycle", "draw process", "draw procedures", "draw software",
            "construction disbursement", "payment disbursement", "fund management",
            "loan administration", "construction loan administration", "cla",
            "draw agent", "draw review", "draw approval", "draw efficiency",
            "draw operations", "draw management software", "construction draw"
        ]
    },
    "Portfolio Visibility & Reporting": {
        "subcategories": [
            "Portfolio oversight",
            "Reporting, analytics",
            "Asset management",
            "Early risk signals"
        ],
        "keywords": [
            "portfolio", "reporting", "analytics", "dashboard", "visibility",
            "asset management", "risk signals", "early warning", "monitoring",
            "performance metrics", "data analytics", "risk indicators", "insights",
            "portfolio management", "portfolio oversight", "portfolio visibility",
            "portfolio monitoring", "portfolio reporting", "asset manager",
            "portfolio analytics", "risk dashboard", "portfolio tracking",
            "project analytics", "real-time monitoring", "portfolio intelligence",
            "portfolio strategy", "portfolio leaders", "portfolio managers"
        ]
    },
    "Risk, Compliance & Governance": {
        "subcategories": [
            "Compliance",
            "Lien, title, COI",
            "Regulatory risk",
            "Fraud prevention"
        ],
        "keywords": [
            "compliance", "regulatory", "lien", "title", "coi", "certificate of insurance",
            "fraud", "risk management", "governance", "due diligence", "documentation",
            "legal", "audit", "regulations", "lien monitoring", "title solutions",
            "lien waiver", "compliance tracking", "risk mitigation", "risk assessment",
            "risk monitoring", "compliance officer", "risk officer", "credit risk",
            "regulatory risk", "fraud prevention", "compliance risk", "examination",
            "audit trail", "governance policy", "risk framework"
        ]
    },
    "Origination → Post-Close Continuity": {
        "subcategories": [
            "Origination pipeline",
            "Deal management",
            "Handoffs between systems"
        ],
        "keywords": [
            "origination", "pipeline", "deal", "management", "handoff", "transition",
            "post-close", "continuity", "workflow", "process", "integration",
            "deal tracking", "customer journey", "origination pipeline",
            "deal management", "loan origination", "origination system",
            "system handoff", "workflow integration", "underwriting",
            "loan closing", "closing procedure", "origination process",
            "credit teams", "underwriters", "origination leaders"
        ]
    },
    "AI & Decision Intelligence": {
        "subcategories": [
            "AI agents",
            "Automation tied to judgment",
            "Early signals, not just speed"
        ],
        "keywords": [
            "ai", "machine learning", "automation", "intelligence", "decision",
            "predictive", "agents", "algorithm", "signals", "pattern recognition",
            "smart automation", "artificial intelligence", "ai agents", "agentic ai",
            "draw agent", "ai-assisted", "automation", "ai automation", "decision intelligence",
            "predictive analytics", "intelligent automation", "ai-powered",
            "data intelligence", "smart decision", "automation tied to judgment"
        ]
    }
}

# Lender Lifecycle Stages
LIFECYCLE_STAGES = {
    "Origination": {
        "keywords": ["origination", "application", "approval", "underwriting", "qualification",
                     "lead generation", "credit check", "loan application", "pre-qualification"],
        "order": 1
    },
    "Pre-Close Strategic Evaluation": {
        "keywords": ["pre-sale", "strategic evaluation", "vendor evaluation", "pre-close",
                     "evaluation", "due diligence", "technology assessment", "demo"],
        "order": 1.5
    },
    "Funding": {
        "keywords": ["funding", "disbursement", "draw", "capital", "advance",
                     "fund release", "closing", "closing costs", "payment processing"],
        "order": 2
    },
    "Construction": {
        "keywords": ["construction", "build", "progress", "inspection", "milestones",
                     "active construction", "construction phase", "building", "project execution"],
        "order": 3
    },
    "Post-Close": {
        "keywords": ["post-close", "servicing", "monitoring", "management", "ongoing",
                     "portfolio oversight", "active construction", "draw execution",
                     "operational policy", "inspection oversight", "loan servicing"],
        "order": 4
    },
    "Completion": {
        "keywords": ["completion", "perm", "permanent", "conversion", "closeout",
                     "certificate of occupancy", "final inspection", "project closeout"],
        "order": 5
    },
    "Default/Resolution": {
        "keywords": ["default", "delinquent", "foreclosure", "workout", "resolution",
                     "loss mitigation", "default management"],
        "order": 6
    }
}

# ICP (Ideal Customer Profile) Definitions
ICPS = {
    "Construction Lenders": {
        "keywords": ["construction", "builder", "developer", "construction lending",
                     "construction lender", "construction loan", "home builder"],
        "characteristics": ["managing construction projects", "managing drawdowns", "project oversight",
                            "construction loan", "construction finance"]
    },
    "Commercial Real Estate Lenders": {
        "keywords": ["commercial", "cre", "commercial real estate", "multifamily", "office", "retail",
                     "cre lender", "cre lending", "cre finance"],
        "characteristics": ["portfolio management", "asset management", "property management",
                            "commercial lending", "commercial finance"]
    },
    "Banks": {
        "keywords": ["bank", "banking", "regional bank", "community bank", "credit union",
                     "financial institution", "depository"],
        "characteristics": ["loan products", "customer banking", "financial services"]
    },
    "Credit Unions": {
        "keywords": ["credit union", "cu lending", "credit union loan", "cu finance"],
        "characteristics": ["member lending", "cooperative banking", "member services"]
    },
    "Mortgage Servicers": {
        "keywords": ["servicer", "servicing", "mortgage", "loan servicing", "loan administrator"],
        "characteristics": ["loan management", "borrower management", "payment processing",
                            "account servicing", "customer service"]
    },
    "Private Credit Lenders": {
        "keywords": ["private credit", "nonbank", "private lender", "alternative financing"],
        "characteristics": ["alternative financing", "direct lending", "risk-based pricing"]
    },
    "Investment Managers": {
        "keywords": ["investment", "fund", "asset manager", "portfolio manager", "investor"],
        "characteristics": ["portfolio visibility", "reporting", "performance analytics",
                            "investment strategy", "portfolio strategy"]
    },
    "Life Insurance Companies": {
        "keywords": ["life insurance", "insurance company", "policy loan"],
        "characteristics": ["investment products", "policy loans", "asset management"]
    },
    "Risk & Compliance Officers": {
        "keywords": ["compliance", "risk", "audit", "governance", "regulatory", "risk officer", "credit risk"],
        "characteristics": ["risk management", "compliance monitoring", "audit trails",
                            "regulatory oversight", "risk assessment"]
    }
}
