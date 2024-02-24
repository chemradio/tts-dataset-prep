from pathlib import Path
from helpers.convert_audio import convert_audio_48_mono_wav
from df.enhance import enhance, init_df, load_audio, save_audio


def denoise_audio(input_audio_path: Path | str, output_audio_path: Path | str) -> None:
    temp_converted_path = input_audio_path.parent / (
        input_audio_path.stem + "_48mono_tmp.wav"
    )
    convert_audio_48_mono_wav(input_audio_path, temp_converted_path)
    model, df_state, _ = init_df()
    audio, _ = load_audio(temp_converted_path, sr=df_state.sr())
    enhanced = enhance(model, df_state, audio)
    save_audio(output_audio_path, enhanced, df_state.sr())
    temp_converted_path.unlink()


def denoise_folder(folder: dict[Path]) -> dict[Path]:
    if not folder.get("denoised"):
        denoised_folder = folder["folder"] / "denoised"
        denoised_folder.mkdir(exist_ok=True)

        denoised_path = denoised_folder / f"{folder['audio'].stem}_denoised.wav"
        denoise_audio(folder["audio"], denoised_path)
        folder["denoised"] = denoised_path

    return folder
