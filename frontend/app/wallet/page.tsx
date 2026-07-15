"use client";

export default function Page(){
 return (
  <main className="market-page">
   <section className="wallet-panel">
    <h1>💎 BKC Wallet</h1>
    <p className="balance">68.02 BKC</p>
    <div className="wallet-actions">
     <button>Connect Wallet</button>
     <button>Transaction History</button>
    </div>
   </section>
  </main>
 );
}
