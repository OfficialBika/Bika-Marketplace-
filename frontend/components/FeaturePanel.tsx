type Props={title:string;value:string};

export default function FeaturePanel({title,value}:Props){
  return (
    <div className="nft">
      <h3>{title}</h3>
      <p>{value}</p>
    </div>
  );
}
