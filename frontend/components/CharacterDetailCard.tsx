type Character = {
  name?: string;
  image?: string;
  rarity?: string;
  price?: number;
  description?: string;
};

export default function CharacterDetailCard({character}:{character:Character}) {
  return (
    <section className="nft">
      <img src={character.image || "/placeholder.png"} alt={character.name || "Character"} />
      <h2>{character.name}</h2>
      <p>Rarity: {character.rarity}</p>
      <p>{character.description || "Bika Supreme Character"}</p>
      <strong>{character.price || 0} BKC</strong>
      <button>BUY CHARACTER</button>
    </section>
  );
}
