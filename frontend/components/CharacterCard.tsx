type Props = {
  character: {
    name?: string;
    image?: string;
    rarity?: string;
    price?: number;
  }
};

export default function CharacterCard({character}: Props){
  return (
    <article className="nft">
      <img src={character.image || "/placeholder.png"} alt={character.name || "Character"} />
      <h3>{character.name}</h3>
      <p>{character.rarity || "Supreme"}</p>
      <b>{character.price || 0} BKC</b>
      <button>VIEW</button>
    </article>
  );
}
