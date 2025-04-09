import Cookies from 'js-cookie';

if(typeof window !== 'undefined') {
	// If running on the server, don't execute any client-side code
	window.Cookies = Cookies;
}

let scores: number[] = $state([]);
export const sortedScores = () => scores.sort((a, b) => a - b)

export function loadScoreCookie() {
	const cookie = Cookies.get('highscores')
	if (cookie) {
		// Parse the cookie string into an array of numbers
		scores = JSON.parse(cookie);
	} else {
		// If no cookie, generate random scores
		scores = [];
	}
	// Generate random scores between 10 and 200
}


export function saveScoreCookie() {
	// Save the scores to a cookie
	Cookies.set('highscores', JSON.stringify(scores), { path: window.location.pathname });
}

export function addScore(score: number) {
	// Add a new score to the scores array
	scores.push(score);
	// Save the updated scores to the cookie
	saveScoreCookie();
}