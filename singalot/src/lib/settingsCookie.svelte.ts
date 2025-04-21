import Cookies from 'js-cookie';

export const settings = $state({
	playChord: true,
	hideEmoji: false,
})


export function loadSettingsCookie() {
	const settingsCookie = Cookies.get('settings')
	if (settingsCookie) {
		const savedSettings = JSON.parse(settingsCookie);
		if(savedSettings.playChord !== undefined) {
			settings.playChord = savedSettings.playChord;
		}

		if(savedSettings.hideEmoji !== undefined) {
			settings.hideEmoji = savedSettings.hideEmoji;
		}
	}
}


export function saveSettingsCookie(data: typeof settings) {
	// Save the scores to a cookie
	Cookies.set('settings', JSON.stringify(data), { path: window.location.pathname });
}