export async function getMarketplaceStatus(){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/marketplace-flow/status`);
 return res.json();
}
