export async function getSystemStatus(){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/system/version`);
 return res.json();
}
