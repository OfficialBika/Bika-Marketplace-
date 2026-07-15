"use client";

import {useEffect,useState} from "react";
import {getWallet,type Transaction} from "@/lib/api";

export default function Page(){
 const [balance,setBalance]=useState("68.02");
 const [connected,setConnected]=useState(false);
 const [transactions,setTransactions]=useState<Transaction[]>([]);
 const [message,setMessage]=useState("");

 useEffect(()=>{
  getWallet()
   .then(data=>{
    if(data.balance !== undefined) setBalance(String(data.balance));
    if(data.transactions) setTransactions(data.transactions);
   })
   .catch(()=>setMessage("Unable to load wallet data"));
 },[]);

 return (
  <main className="market-page">
   <section className="wallet-panel feature-glow">
    <h1>💎 BKC Wallet</h1>
    <p className="balance">{balance} BKC</p>

    <div className="wallet-actions">
     <button onClick={()=>setConnected(true)}>
      {connected ? "Wallet Connected" : "Connect Wallet"}
     </button>
    </div>

    {message && <p>{message}</p>}

    <h2>Transaction History</h2>
    {transactions.length===0 ? (
      <p>No transactions yet</p>
    ) : transactions.map((tx,i)=>(
      <article className="nft" key={tx.id || i}>
       <p>{tx.type || "Marketplace"}</p>
       <b>{tx.amount || 0} BKC</b>
      </article>
    ))}
   </section>
  </main>
 );
}
