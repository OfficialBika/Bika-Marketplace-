"use client";

import {useState} from 'react';

export default function TradePanel(){
 const [status,setStatus]=useState('');
 const createTrade=()=>setStatus('Trade request created');
 return (
  <section className="trade-panel rounded-3xl border p-6">
   <h2 className="text-xl font-bold">Trade Center</h2>
   <p>Exchange Bika marketplace assets securely.</p>
   <button onClick={createTrade} className="mt-4 rounded-xl px-5 py-2">CREATE TRADE</button>
   {status && <p className="mt-3">{status}</p>}
  </section>
 );
}
