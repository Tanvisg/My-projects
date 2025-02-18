const API_KEY = "7eac924a2cdb0a08b1ca3ebacb4617e5";
const BASE_URL = "https://api.themoviedb.org/3/";
const BASE_URL_2 = "https://api.themoviedb.org/3";
const IMAGE_BASE_URL = "https://image.tmdb.org/t/p";

// export const getPopularMovies = async () => {
//   const response = await fetch(`${BASE_URL}movie/popular?api_key=${API_KEY}`);
//   const text = await response.text();
//   console.log("Raw response:", text);
//   // Then try parsing it if it's not empty:
//   const data = text ? JSON.parse(text) : {};
//   return data.results;
// };

export const getPopularMovies = async () => {
  const response = await fetch(`${BASE_URL}movie/popular?api_key=${API_KEY}`);
  const data = await response.json();
  console.log(data);
  return data.results;
};

export const searchMovies = async (query) => {
  const response = await fetch(
    `${BASE_URL}search/movie?api_key=${API_KEY}&query=${encodeURIComponent(
      query
    )}`
  );
  const data = await response.json();
  console.log(data);
  return data.results;
};

// const response = await fetch(`${BASE_URL}/movie/popular?api_key=${API_KEY}`);
// const text = await response.text();

// return data.results;
