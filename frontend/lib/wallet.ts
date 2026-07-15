export async function getWallet(userId:string){
  const base = process.env.NEXT_PUBLIC_API_URL;
  const res = await fetch(`${base}/wallet/${userId}`, {
    cache: "no-store"
  });
  return res.json();
}
