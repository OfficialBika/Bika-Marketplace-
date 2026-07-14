export default function Home(){
 const menus=['Rewards','Wallet','Gate','Trade','Cleaning','Purchase','NFT','Auction'];
 return <main className="min-h-screen bg-[#090014] text-white p-6">
  <h1 className="text-4xl font-bold">Bika Marketplace</h1>
  <p className="mt-2 text-pink-400">BKC Character Trading Hub</p>
  <div className="grid grid-cols-2 gap-4 mt-10">
   {menus.map(x=><div key={x} className="rounded-3xl border border-purple-500/30 bg-white/5 p-8 text-center">{x}</div>)}
  </div>
 </main>
}
