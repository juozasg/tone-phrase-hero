// import { SplendidGrandPiano, Reverb } from "smplr";
import { SvelteMap } from "svelte/reactivity";
import { blackSemitones, type Mood } from "./names";

// make ios/safari happy
if(typeof window !== 'undefined') {
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	const AudioContext = window.AudioContext || (window as any).webkitAudioContext;
	new AudioContext();
}

const chordsAudioBase64Data = new SvelteMap<string, string>();


let audioIsLoaded = $state(false);
let audioInitialized = $state(false);

export const isLoadingAudio = () => !audioIsLoaded;

const blobToBase64 = (blob: Blob) => {
  const reader = new FileReader();
  reader.readAsDataURL(blob);
  return new Promise(resolve => {
    reader.onloadend = () => {
      resolve(reader.result);
    };
  });
};

async function loadChordData(st: number, mood: Mood) {
	const dataKey = `${st}-${mood}`;
	const audioFile = `/${st}-${mood}.mp3`;
	const response = await fetch(audioFile);
	if (!response.ok) {
		console.error(`Failed to load audio file: ${audioFile}`);
		return;
	}

	const audioBlob = await response.blob();
	const audioUrl = await blobToBase64(audioBlob);

	// console.log('audioFile loaded', audioFile, audioBlob.size);
	chordsAudioBase64Data.set(dataKey, audioUrl as string);
}

export async function loadAudioData() {
	const promises: Promise<void>[] = [];

	blackSemitones.forEach((st) => {
		['happy', 'sad'].forEach((mood) => {
			promises.push(loadChordData(st, mood as Mood))
		});
	})

	await Promise.all(promises);
	audioIsLoaded = true;
}


export async function initAudioInteraction() {
	if (audioInitialized) return;
	const audio = document.getElementById('audio') as HTMLAudioElement;
	console.log('playing init audio', audio);
	await audio.play();

	console.log('init audio done playing');

	audioInitialized = true;
}


export function playChord(rootSt: number, mood: Mood) {
	if (!audioInitialized) {
		console.log('Audio not initialized');
		return;
	}

	if (!audioIsLoaded) {
		console.log('Audio not loaded');
		return;
	}

	const dataKey = `${rootSt}-${mood}`;
	// const dataKey = '1-happy';
	const base64Data = chordsAudioBase64Data.get(dataKey);
	if (!base64Data) {
		console.log(`Audio data not found for ${dataKey}`);
		return;
	}

	const audio = document.getElementById('audio') as HTMLAudioElement;

	audio!.src = base64Data;
	// audio!.currentTime = 0;
	audio!.pause();

	setTimeout(() => {
		// audio!.currentTime = 0;
		audio!.play();
	}, 0);
}


