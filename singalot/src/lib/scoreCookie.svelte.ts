import Cookies from 'js-cookie';

if (typeof window !== 'undefined') {
	// If running on the server, don't execute any client-side code
	window.Cookies = Cookies;
}

let scores = $state(
	{
		'lesson01': [] as number[],
		'lesson02': [] as number[],
		'lesson03': [] as number[],
	}
);

// export const sortedScores = () => scores.sort((a, b) => a - b)
export const sortedScores = () => [[300, 'lesson01'], [200, 'lesson02'], [300, 'lesson03']];

export const bestScore = (level: keyof typeof scores) => {
	const levelScores = scores[level];
	if (!levelScores || levelScores.length === 0) {
		return;
	}
	return Math.min(...levelScores);
}



export function loadScoreCookie() {
	const cookie = Cookies.get('levelscores')
	if (cookie) {
		// Parse the cookie string into an array of numbers
		scores = JSON.parse(cookie);
	} else {
		scores = {
			'lesson01': [200, 250],
			'lesson02': [200],
			'lesson03': [300],
		};
		saveScoreCookie();
	}

	console.log('Loaded scores from cookie:', scores);
}


export function saveScoreCookie() {
	// Save the scores to a cookie
	Cookies.set('levelscores', JSON.stringify(scores), { path: window.location.pathname });
}

export function addScore(score: number) {
	// Add a new score to the scores array
	// scores.push(score);
	scores['lesson01'].push(score);
	// Save the updated scores to the cookie
	saveScoreCookie();
}