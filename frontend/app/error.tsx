"use client";

type ErrorProps={
 error: Error & { digest?: string };
 reset: () => void;
};

export default function Error({error, reset}: ErrorProps){
 return (
  <main className="market-page">
   <section className="purchase-panel feature-glow">
    <h1>Something went wrong</h1>
    <p>{error.message || "Marketplace loading error."}</p>
    <button onClick={()=>reset()}>TRY AGAIN</button>
   </section>
  </main>
 );
}
