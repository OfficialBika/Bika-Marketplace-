import { coinDisplayName } from '@/lib/names';

export default function AuctionCard({name,bid,endsAt}:{name:string;bid:number;endsAt?:string}){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-5 backdrop-blur">
   <h3 className="text-xl font-bold">{name}</h3>
   <p>Current Bid: {bid} {coinDisplayName}</p>
   {endsAt && <p className="text-sm">Ends: {endsAt}</p>}
   <button className="mt-4 rounded-xl bg-blue-600 px-5 py-2">Bid</button>
  </div>
}
