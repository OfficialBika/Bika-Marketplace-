import { coinDisplayName } from '@/lib/names';

export default function WalletCard({balance, address}:{balance:number; address?:string}){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-6">
   <div className="text-sm opacity-70">Wallet Balance</div>
   <div className="text-3xl font-bold">{balance} {coinDisplayName}</div>
   {address && <div className="mt-2 text-xs opacity-70">{address}</div>}
  </div>
}
