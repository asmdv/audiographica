import React, { useContext, useEffect, useState } from "react";
import './Home.css'

const Home = () => {
    return (
        <div>
            <div class=" huge ui inverted  top fixed black secondary pointing menu" id="navbar">
                <a class="item">
                Music to Notes <i class="music icon"></i>                 
                </a>
            <div class="right menu">
                 <a class="ui item" href="https://github.com/Asif-Mammadov/music-to-notes/tree/main/">
                    Report
                </a>
                <a class="item" href="https://github.com/Asif-Mammadov/music-to-notes/tree/main/">
                    Project Codes<i class="github icon"></i>
                </a>

            </div>
        </div>
            <h1>Song to Sheet Music</h1>
            <h2>Translate any song to the sheet music format to play it on any instrument.</h2>
            
 
        </div>
    );
  };
  
  export default Home;