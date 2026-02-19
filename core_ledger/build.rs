fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Tell tonic-build to compile our proto definition
    tonic_build::compile_protos("../proto/sentinel.proto")?;
    Ok(())
}