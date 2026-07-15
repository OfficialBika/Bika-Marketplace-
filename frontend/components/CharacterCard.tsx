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
    <article className="character-card rounded-2xl border p-4">
      {character.image && <img src={character.image} alt={character.name || 'Character'} />}
      <h3>{character.name}</h3>
      <p>{character.rarity}</p>
      <span>{character.price || 0} BKC</span>
    </article>
  );
}
