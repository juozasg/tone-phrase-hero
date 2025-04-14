<script lang="ts">
	import { isLoadingAudio } from './audio.svelte';
	import { loadSettingsCookie, saveSettingsCookie, settings } from './settings.svelte';


	loadSettingsCookie();
	$effect(() => {
		saveSettingsCookie(settings);
	});
</script>

{#if isLoadingAudio()}
	<div class="container">Loading audio...</div>
{:else}
	<div class="container">
		<div class="columns">
			<div class="column options-column">OPTIONS</div>
			<div class="column play-chord-column">
				<input id="play-chord" type="checkbox" bind:checked={settings.playChord} />
				<label for="play-chord">Play Chord</label>
			</div>
			<div class="column hide-emoji-column">
				<input id="hide-emoji" type="checkbox" bind:checked={settings.hideEmoji} />
				<label for="hide-emoji">Hide Mood Emoji</label>
			</div>
		</div>
	</div>
{/if}

<style>
	.container {
		position: fixed;
		bottom: 64px;
		left: 0;
		width: 100%;
		color: #777;
	}

	.column {
		display: block;
		justify-content: left;
		text-align: left;
	}

	.options-column {
		min-width: 90px;
		max-width: 90px;
		justify-content: right;

		font-weight: 500;
	}

	.play-chord-column {
		min-width: 115px;
		max-width: 115px;
	}

	.hide-emoji-column {
		min-width: 170px;
		max-width: 170px;
	}

	input[type='checkbox'] {
		position: relative;
		bottom: -1px;
	}

	label {
		cursor: pointer;
	}
</style>
