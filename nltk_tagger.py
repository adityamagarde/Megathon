#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:32:52 2018

@author: adityamagarde
"""

import spacy
from spacy import displacy
from collections import Counter
from spacy.lang.en.examples import sentences

nlp = spacy.load('en')

str = ['Resume', 'CV', 'Curriculum Vitae', 'Yee Choon Kit', '547 Serangoon North Ave 3', '#12-162', 'Singapore 550547', '+65 9725 8036', 'choonkit.yee@gmail.com', 'EDUCATION', '2006 - 2010', 'Singapore Management University (SMU)', 'Bachelor in Social Sciences (Honours)', 'Double Majors in Political Science & Finance', 'WORK EXPERIENCE', 'Sept 2015  Current   ABN AMRO Clearing Bank N.V., Relationship Manager', '\uf0b7  Managing pool of hedge fund, proprietary trading clients', 'trading multi asset classes', '\uf0b7  Contributed to 20% increase of revenue for my pool of clients', 'in FY 2016', '\uf0b7  Onboarding clients through effective management and', 'communication to internal stakeholders eg. Operations, Risk,', 'Technical teams', 'Increasing ROE by efficient allocation of clients credit line', '\uf0b7', '\uf0b7  Strong understanding of Treasury and SBL services', '\uf0b7', 'In-depth knowledge of APAC equities & global', 'futures/options markets', '\uf0b7  ETF creation/redemption expertise accumulated through', 'working with fund managers', '\uf0b7  Opening up new markets and products offerings to clients', '\uf0b7  Adhering and performing due diligence checks and annual', 'compliance reviews for clients', '\uf0b7  Strong negotiation skills for fees renewal and enforcement of', 'tighter global regulatory requirements', '\uf0b7  Preparing client risk management and credit proposals', '\uf0b7  Appointed Co-Chairman for ABN AMRO Banks 2016 One', 'Bank One Team initiative', 'Oct 2014  Sept 2015  Mizuho Securities (S) Pte Ltd, Asst. Vice President, Futures Sales', '\uf0b7  Spearheaded Mizuho Securities Asia  ex Japan sales for', 'futures & OTC swaps clearing and execution', '\uf0b7  Cross selling of financial products with corporate bankers', 'from Mizuho Bank', '\uf0b7  Opened up new markets in South East Asia and Greater China', '\uf0b7  Established relationships with major energy/commodity', 'traders (Sinopec, Unipec, Petronas, Vitol etc), financial', 'institutions (Standard Chartered Bank, China Merchant Bank', 'etc) & brokers', '\uf0b7', 'Initiated the companys first foray into the Taiwanese market', 'by working with several top Taiwanese FCMs', '\uf0b7  Negotiated and brokered the companys first Introducer', '\uf0b7', 'Agreement with Neo & Partners, a local trading arcade', 'Implemented cost saving strategies and increasing sales', 'figures by 25% to improve department P&L for FY 2014', '\uf0b7  Preparing credit reports and risk reviews for risk committee', '\uf0b7  Preparing KYC documents for new client onboarding', '\uf0b7  Part of the working group for companys MAS audit in 2014', 'Jan 2011  Oct 2014  Phillip Securities Pte Ltd, Senior Dealer', '\uf0b7  Headed the global and institutional sales at Contracts for', 'Difference (CFD) Department', '\uf0b7  Started CFD prime service business and onboarded Baiduri', 'Bank for white labeling business', '\uf0b7  Overseeing CFD business for Phillip Capital Australia and', 'started an Asian CFD dealing desk to capture Asian AUM', '\uf0b7  Managing clients investment portfolio of US$10 million by', 'providing investment strategies and trade execution services', '\uf0b7  Structuring new CFD equity markets for trading with', 'counterparties Morgan Stanley & Deutsche Bank', '\uf0b7  Led a team of business analysts and crafted the ASX Equity &', 'Index CFDs in 2013', '\uf0b7  Mentoring junior dealers with potential to head the CFD', 'business in Australia and UK offices', '\uf0b7  Concluded the departments first Introducer Broker', 'Agreement with a Taiwanese investment fund', '\uf0b7  Presented at local and overseas investment seminars', 'PROFESSIONAL CERTIFICATIONS', '\uf0b7  MAS Licensed Trading Representative (Rep No: YCK300028559)', '\uf0b7  CMFAS M1, M2A, M5, M6, M6A & M8 certified', '\uf0b7  Professional Chinese in Finance & Accounting Certification from NTU', 'LANGUAGE & IT SKILLS', '\uf0b7  Proficient in Microsoft Word, Excel & PowerPoint', '\uf0b7  Native speaker in English, Mandarin & fluent in Cantonese', '\uf0b7  Knowledge in FIX connectivity', '\uf0b7  Experience in using Trading Technologies, CQG trading platforms, Bloomberg EMSX']

for i in str:
    doc = nlp(i)
    for X in doc.ents:
        if X.label_ == 'PERSON':
            print('Names: ', X.text)
        elif X.label_ == 'GPE':
            print('Places: ', X.text)
        elif X.label_ == 'DATE':
            print('Organizations: ', X.text)