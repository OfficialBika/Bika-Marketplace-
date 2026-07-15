"use client";

import Link from "next/link";

export default function CharacterPage({params}:{params:{id:string}}){
 return (
  <main className="market-page">
   <section className="nft feature-glow">
    <h1>🔥 Character Detail</h1>
    <h2>{params.id}</h2>
    <p>Supreme marketplace character information.</p>
    <div>
     <p>Rarity: Supreme Limited</p>
     <p>Status: Available</p>
    </div>
    <Link className="purchase-btn" href={`/purchase?character=${params.id}`}>
     BUY CHARACTER
    </Link>
   </section>
  </main>
 );
}
