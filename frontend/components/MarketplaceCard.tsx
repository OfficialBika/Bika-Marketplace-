import { nftDisplayName, coinDisplayName } from '@/lib/names';

export default function MarketplaceCard({name, price}:{name:string;price:number}){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-5 backdrop-blur">
   <h3 className="text-xl font-bold">{nftDisplayName}</h3>
   <p>{name}</p>
   <p className="mt-3">{price} {coinDisplayName}</p>
   <button className="mt-4 rounded-xl px-5 py-2 bg-purple-600">Purchase</button>
 </div>
}
