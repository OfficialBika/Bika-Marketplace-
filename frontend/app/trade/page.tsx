"use client";

import {useEffect,useState} from "react";
import {getTrades} from "@/lib/api";

export default function Page(){
 const [trades,setTrades]=useState<any[]>([]);

 useEffect(()=>{
  getTrades()
   .then(data=>setTrades(data?.trades || []))
   .catch(()=>{});
 },[]);

 return (
  <main className="market-page">
   <section className="trade-panel">
    <h1>🔄 Character Trade</h1>
    <p>Create and manage character exchange requests.</p>
    <button>Create Trade Request</button>

    <h2>Active Requests</h2>
    {trades.length===0 ? (
     <p>No active trades</p>
    ) : trades.map((t,i)=>(
     <article key={i} className="nft">
      <p>{t.name || "Character Trade"}</p>
     </article>
    ))}
   </section>
  </main>
 );
}
