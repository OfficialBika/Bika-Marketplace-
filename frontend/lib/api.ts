export async function getFeaturedCharacters(){
  const url = process.env.NEXT_PUBLIC_API_URL;
  const res = await fetch(`${url}/characters/featured`, {
    cache: "no-store"
  });
  return res.json();
}
