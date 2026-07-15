export async function getReadiness(){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/system/readiness`);
 return res.json();
}
