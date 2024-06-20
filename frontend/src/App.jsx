import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3000/news'); // Replace with your server URL and endpoint
        setData(response.data); // Assuming your server responds with an array of data
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);
  return (
    <div>
      <h1>Headlines from google news</h1>
      <ul>
        {data.map((item, index) => (
          <li key={index}>
            <strong>{item.title}</strong>
            <br />
            {item.channel !== "No Channel" ? (
                  <>
                    <em>Channel: {item.channel}</em>
                    <br />
                    {item.context && <span>{item.context}</span>}
                  </>)  
                  : 
                (<span>{item.context}</span>)}
          </li>
          ))}
      </ul>
    </div>
  );
};

export default App;
