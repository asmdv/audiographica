import { useState} from 'react';
import { Image } from './Image';
import axios from 'axios';

export const FileUploader =  ({})=>{
    const [file,setFile] = useState(null);
    const [img,setImg] = useState("");

    const onInputChange = (e)=>{
        console.log(e.target.files)
        setFile(e.target.files[0])
    };

    const onSubmit = (e) =>{
        e.preventDefault();
        const data = new FormData();
        data.append('file', file );

        axios.post('http://localhost:5000/api/audio',data)
            .then((e)=>{
                console.log("Successfuly sent the file to server")
                console.log(e.data.path)
                // var image_path = process.env.PUBLIC_URL+"/notes.png"
                setImg("/notes.png");
                console.log("updated image");
                console.log("Image is",img)

            })
            .catch((e)=>{
                console.log('Error',e)
            })
    };
  

    return(<div>  
                <form method="post" action="#" id="#" onSubmit={onSubmit}>            
                        <label htmlFor="files" className="ui huge inverted button">Upload Song File </label>
                        <input id="files" type="file"
                               onChange={onInputChange} 
                               multiple=""
                               style={{visibility: 'hidden'}}
                               />

                    <button className="ui submit button">Submit</button>
                </form>
                <Image img={img} />
        
               
            </div>
  )
};