import { SplendidGrandPiano, Reverb } from "smplr";
import type { Mood } from "./names";

let audioContext: AudioContext | undefined;
let piano: SplendidGrandPiano;


export function getAudioContext(): AudioContext | undefined {
	return audioContext;
}

export function initAudio() {
	audioContext = new AudioContext();

	piano = new SplendidGrandPiano(audioContext, {
		notesToLoad: {
			notes: Array.from({ length: 21 }, (_, i) => i + 60),
			velocityRange: [80, 127],
		},
	});

	console.log('loading piano');
	piano.load.then(() => {
		console.log('piano LOADED');
		piano.output.addEffect("reverb", new Reverb(audioContext!), 0.1);

		window['piano'] = piano;


	});
}

export function playChord(rootSt: number, mood: Mood) {
	if(!audioContext && !rootSt && !mood) {
		console.error('AudioContext not initialized or invalid parameters');
		return;
	}
	rootSt = rootSt + 60;
	const now = audioContext!.currentTime;
	piano.start({ note: rootSt, velocity: 100, duration: 0.6, time: now });
	piano.start({ note: rootSt + 12, velocity: 100, duration: 0.6, time: now });
	piano.start({ note: rootSt + (mood == 'happy' ? 4 : 3), velocity: 100, duration: 0.6, time: now + 0.01 });
	piano.start({ note: rootSt + 7, velocity: 100, duration: 0.6, time: now + 0.02 });
}





// const piano = new SplendidGrandPiano(audioContext, {
// 	notesToLoad: {
// 		notes: Array.from({ length: 21 }, (_, i) => i + 60),
// 		velocityRange: [80, 127],
// 	},
// });

// console.log('loading piano');
// piano.load.then(() => {
// 	console.log('piano LOADED');
// 	piano.output.addEffect("reverb", new Reverb(audioContext), 0.1);
// 	piano.start({ note: "C#4", velocity: 100, duration: 1 });
// 	piano.start({ note: "F", velocity: 100, duration: 1 });
// 	piano.start({ note: "G#4", velocity: 100, duration: 1 });
// });

// if (typeof window !== 'undefined') {
// 	window['piano'] = piano;
// }



