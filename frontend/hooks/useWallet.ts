import {useEffect,useState} from 'react';

export function useWallet(address?:string){
 const [balance,setBalance]=useState(0);
 const [connected,setConnected]=useState(false);

 useEffect(()=>{
  if(!address){setConnected(false); return;}
  const api=process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
  fetch(`${api}/wallet/${address}`)
   .then(r=>r.json())
   .then(d=>{setBalance(d.balance||0); setConnected(true);})
   .catch(()=>{setBalance(0); setConnected(false);});
 },[address]);

 return {balance, connected};
}
