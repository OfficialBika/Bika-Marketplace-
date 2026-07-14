# 🚀 Bika Marketplace

A next-generation Mini Web Marketplace built for **Bika Characters**.

## ✨ Vision

Bika Marketplace is designed as a secure NFT-style character trading platform powered by:

- Next.js Frontend
- FastAPI Backend
- MongoDB Database
- BKC Economy System

The existing `bika_bot` database is protected. Marketplace features extend the system without destructive changes to existing character data.

---

## 🏗 Architecture

```
Bika Marketplace
│
├── frontend
│   └── Next.js + TypeScript
│       ├── NFT Cards
│       ├── Spin Wheel
│       ├── Wallet UI
│       ├── Auction UI
│       └── Theme System
│
└── backend
    └── FastAPI
        ├── Character Service
        ├── Marketplace API
        ├── Wallet System
        ├── Auction Engine
        └── Transaction Security
```

## 🗄 Database Strategy

Database:

```
bika_bot
```

Existing data:

- Characters
- Users
- Inventory

Marketplace extensions:

- marketplace_listings
- marketplace_orders
- auctions
- bids
- trades
- wallet_transactions
- spin_history
- audit_logs

Existing character data is never deleted by Marketplace operations.

## 💎 BKC Economy

Default Coin:

```
BKC
```

Configurable through environment variables.

## 🎮 Features

### Bika Characters

- Character Gallery
- NFT Card View
- Rarity System
- Ownership Tracking

### Marketplace

- Buy / Sell
- Listings
- Search
- Filters

### Auction

- Create Auction
- Bidding
- Winner Selection
- History Tracking

### Spin Wheel

- Rewards
- BKC Drops
- Rare Character Drops
- Spin History

### Wallet

- BKC Balance
- Transactions
- Reward Logs

## 🎨 Theme System

Supported themes:

- Neon
- RedBlue

Change with ENV:

```
NEXT_PUBLIC_THEME=neon
```

## ⚙️ Environment Configuration

Example:

```
NEXT_PUBLIC_NFT_NAME=BIKA
NEXT_PUBLIC_COIN_NAME=BKC
NEXT_PUBLIC_CHARACTER_NAME=Bika Characters
NEXT_PUBLIC_THEME=neon
```

## 🔐 Security Principles

- Protected character ownership
- Transaction validation
- Audit logs
- Error handling
- Safe database operations

## 🛠 Development

Frontend:

```
cd frontend
npm install
npm run dev
```

Backend:

```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

Built for the Bika ecosystem with scalable architecture and production readiness.
