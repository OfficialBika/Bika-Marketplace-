"use client";

import {useState} from 'react';

export default function AuctionPanel(){
 const [message,setMessage]=useState('');
 return (
  <section className="auction-panel rounded-3xl border p-6">
   <h2 className="text-xl font-bold">Auction Center</h2>
   <p>Bid and manage marketplace auctions.</p>
   <button onClick={()=>setMessage('Auction started')} className="mt-4 rounded-xl px-5 py-2">START BID</button>
   {message && <p className="mt-3">{message}</p>}
  </section>
 );
}
