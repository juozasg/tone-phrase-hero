<script lang="ts">
	import type { Mood } from "./names";

	interface Props {
		key: string;
		mood: Mood
		answerOnClick: (key: string, keyEnharmonic: string, mood: 'happy' | 'sad') => void;
	}



	const { key, mood, answerOnClick }: Props = $props();
</script>

<div class="answers">
	<!-- C# key -->
	<button class="btn btn-primary" onclick={() => answerOnClick('C#', 'sad')}>Cis moll</button>
	<button class="btn btn-primary" onclick={() => answerOnClick('C#', 'happy')}>Des dur</button>


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
