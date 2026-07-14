"use client";

import { useState } from 'react';

const rewards = ['BKC', 'Mystical', 'Divine', 'Free Spin'];

export default function SpinWheel(){
 const [result,setResult] = useState('');
 const spin = () => {
  setResult(rewards[Math.floor(Math.random()*rewards.length)]);
 };

 return <div className="rounded-3xl border border-white/20 bg-black/30 p-8 text-center">
   <div className="mx-auto h-56 w-56 rounded-full border-8 border-purple-400 flex items-center justify-center animate-pulse">
    SPIN
   </div>
   <button onClick={spin} className="mt-6 rounded-xl bg-purple-600 px-6 py-3">Spin</button>
   {result && <div className="mt-4">Reward: {result}</div>}
 </div>
}
