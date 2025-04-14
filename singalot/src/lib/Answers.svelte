<script lang="ts">
	import { germanNames, type Semitone } from "./names";

	interface Props {
		semitone: Semitone;
		mood: 'happy' | 'sad';
		onAnswered: (correct: boolean) => void;
	}
	const { semitone, mood, onAnswered }: Props = $props();

	// $effect(() => {
	// 	console.log('ANS semitone', semitone);
	// 	console.log('ANS mood', mood);
	// })

</script>

<div class="answers">
	{#each [1, 3, 6, 8, 10] as st}
		<button class="btn btn-primary" onclick={() => onAnswered(st == semitone && mood == 'sad')}>{germanNames(st as any, 'sad')}</button>
		<button class="btn btn-primary" onclick={() => onAnswered(st == semitone && mood == 'happy')}>{germanNames(st as any, 'happy')}</button>
	{/each}
</div>

<style>
	.btn {
		margin: 3px;
	}
	.answers {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}
</style>
