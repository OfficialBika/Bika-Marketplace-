export async function getConfig(){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/config`);
 return res.json();
}
