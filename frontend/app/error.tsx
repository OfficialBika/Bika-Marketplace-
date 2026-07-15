"use client";

export default function Error({reset}:{error:Error & {digest?:string};reset:()=>void}){
 return (
  <main className="market-page">
   <section className="purchase-panel feature-glow">
    <h1>Something went wrong</h1>
    <p>Marketplace loading error.</p>
    <button onClick={()=>reset()}>TRY AGAIN</button>
   </section>
  </main>
 );
}
