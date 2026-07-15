"use client";

import {useEffect,useState} from "react";
import {getTrades,type Trade} from "@/lib/api";

export default function Page(){
 const [trades,setTrades]=useState<Trade[]>([]);
 const [message,setMessage]=useState("");

 useEffect(()=>{
  getTrades()
   .then(data=>setTrades(data.trades || []))
   .catch(()=>setMessage("Unable to load trades"));
 },[]);

 return (
  <main className="market-page">
   <section className="trade-panel feature-glow">
    <h1>🔄 Character Trade</h1>
    <p>Create and manage character exchange requests.</p>
    <button>Create Trade Request</button>

    {message && <p>{message}</p>}

    <h2>Active Requests</h2>
    {trades.length===0 ? (
      <p>No active trades</p>
    ) : trades.map((t,i)=>(
      <article key={t.id || i} className="nft">
       <p>{t.name || "Character Trade"}</p>
      </article>
    ))}
   </section>
  </main>
 );
}
