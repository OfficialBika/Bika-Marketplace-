"use client";

import {useEffect,useState} from "react";
import {getWallet} from "@/lib/api";

export default function Page(){
 const [balance,setBalance]=useState("68.02");
 const [connected,setConnected]=useState(false);

 useEffect(()=>{
  getWallet()
   .then(data=>{
    if(data?.balance) setBalance(String(data.balance));
   })
   .catch(()=>{});
 },[]);

 return (
  <main className="market-page">
   <section className="wallet-panel">
    <h1>💎 BKC Wallet</h1>
    <p className="balance">{balance} BKC</p>
    <div className="wallet-actions">
     <button onClick={()=>setConnected(true)}>
      {connected ? "Wallet Connected" : "Connect Wallet"}
     </button>
     <button>Transaction History</button>
    </div>
   </section>
  </main>
 );
}
