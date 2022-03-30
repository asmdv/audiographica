import "./style.css";

export const Image = ({img})=>{
        return ( 
            <div id="display">
                {/* <a className="ui inverted green button" id="download" href={img[0]} download><i className="download icon"></i>Click to download </a> */}
                {/* <button className="ui inverted red button" > Clear </button> */}
               <img src={img} alt="Sheet Music failed to upload" />
            </div>);
};