import { SplendidGrandPiano, Reverb } from "smplr";
import type { Mood } from "./names";

let audioContext: AudioContext | undefined;
let piano: SplendidGrandPiano;


let _isLoadingAudio = $state(true);

export const isLoadingAudio = () => _isLoadingAudio

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
		_isLoadingAudio = false;
		piano.output.addEffect("reverb", new Reverb(audioContext!), 0.1);

		// eslint-disable-next-line @typescript-eslint/no-explicit-any
		const w = window as any;
		w['piano'] = piano;
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


