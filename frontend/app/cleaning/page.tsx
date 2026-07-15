"use client";

import {useState} from "react";

export default function Page(){
 const [message,setMessage]=useState("");

 function start(){
  setMessage("Character cleaning process started");
 }

 return (
  <main className="market-page">
   <section className="purchase-panel feature-glow">
    <h1>🧹 Character Cleaning</h1>
    <p>Manage character maintenance and upgrades.</p>
    <button onClick={start}>START CLEANING</button>
    {message && <p>{message}</p>}
   </section>
  </main>
 );
}
