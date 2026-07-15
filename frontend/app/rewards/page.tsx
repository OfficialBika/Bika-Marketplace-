"use client";

import {useState} from "react";

export default function Page(){
 const [message,setMessage]=useState("");

 function claim(){
  setMessage("Reward claim request submitted");
 }

 return (
  <main className="market-page">
   <section className="purchase-panel feature-glow">
    <h1>🎁 Rewards Center</h1>
    <p>Claim marketplace rewards and bonuses.</p>
    <button onClick={claim}>CLAIM REWARD</button>
    {message && <p>{message}</p>}
   </section>
  </main>
 );
}
