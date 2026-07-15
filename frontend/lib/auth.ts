export async function telegramLogin(user:any){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/auth/telegram`,{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify(user)
 });
 return res.json();
}
