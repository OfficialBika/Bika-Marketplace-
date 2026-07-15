"use client";

import {useEffect,useState} from "react";
import {getAuctions} from "@/lib/api";

export default function Page(){
 const [auctions,setAuctions]=useState<any[]>([]);

 useEffect(()=>{
  getAuctions()
   .then(data=>setAuctions(data?.auctions || []))
   .catch(()=>{});
 },[]);

 return (
  <main className="market-page">
   <section className="auction-panel">
    <h1>🏆 Character Auction</h1>
    <p>Browse premium character auctions and bidding.</p>
    <button>View Live Auctions</button>

    <div className="nft-grid">
     {auctions.length===0 ? (
      <p>No live auctions</p>
     ) : auctions.map((item,i)=>(
      <article className="nft" key={i}>
       <h3>{item.name || "Supreme Character"}</h3>
       <p>{item.bid || 0} BKC</p>
       <button>PLACE BID</button>
      </article>
     ))}
    </div>
   </section>
  </main>
 );
}
