import { useState } from 'react';
import axios from 'axios';

export const FileUploader =  ({})=>{
    const [file,setFile] = useState(null);


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
            })
            .catch((e)=>{
                console.log('Error',e)

            })


    };

    return(<div>  
                <form method="post" action="#" id="#" onSubmit={onSubmit}>            
                        <label for="files" class="ui huge inverted button">Upload Song File </label>
                        <input id="files" type="file"
                               onChange={onInputChange} 
                               multiple=""
                               style={{visibility: 'hidden'}}
                               />
        
                    <button class="ui submit button">Submit</button>
                </form>
            </div>
  )
};