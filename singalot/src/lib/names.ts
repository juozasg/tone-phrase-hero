export type Mood = 'happy' | 'sad';

export const semitomes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] as const;
// ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
export const whiteSemitones = [0, 2, 4, 5, 7, 9, 11] as const;
//  ['C#', 'D#', 'F#', 'G#', 'A#'];
export const blackSemitones = [1, 3, 6, 8, 10] as const;

export type Semitone = typeof semitomes[number];
export type WhiteSemitone = typeof whiteSemitones[number];
export type BlackSemitone = typeof blackSemitones[number];


export const semitoneNamesSharps = [
	'C',
	'C#',
	'D',
	'D#',
	'E',
	'F',
	'F#',
	'G',
	'G#',
	'A',
	'A#',
	'B',
	'H'
] as const;

export const semitoneNamesFlats = [
	'C',
	'Db',
	'D',
	'Eb',
	'E',
	'F',
	'Gb',
	'G',
	'Ab',
	'A',
	'B',
	'H'
] as const;

export function getSemitone(key: string) {
	if(semitoneNamesSharps.includes(key as typeof semitoneNamesSharps[number])) {
		return semitoneNamesSharps.indexOf(key as typeof semitoneNamesSharps[number]);
	}

	if(semitoneNamesFlats.includes(key as typeof semitoneNamesFlats[number])) {
		return semitoneNamesFlats.indexOf(key as typeof semitoneNamesFlats[number]);
	}

	alert(`Key ${key} not found`);
	console.error(`Key ${key} not found`);
	return 0;
}

// export const enharmonics = {
// 	'C#': 'Db',
// 	'D#': 'Eb',
// 	'F#': 'Gb',
// 	'G#': 'Ab',
// 	'A#': 'Bb'
// };

// export const germanNames = {
// 	'Db'


