export async function getTransactions(userId:string){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/wallet/${userId}`);
 return res.json();
}
