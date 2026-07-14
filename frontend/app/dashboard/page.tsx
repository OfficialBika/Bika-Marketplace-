import DashboardStats from '@/components/DashboardStats';

export default function DashboardPage(){
 const stats = [
  {title:'Characters', value:'0'},
  {title:'BKC Balance', value:'0'},
  {title:'Auctions', value:'0'}
 ];

 return <main className="p-6">
  <h1 className="text-3xl font-bold mb-6">Bika Marketplace Dashboard</h1>
  <DashboardStats stats={stats}/>
 </main>
}
